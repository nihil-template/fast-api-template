"""이메일 발송 유틸리티"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

from src.settings import settings


def send_reset_password_email(
  to_email: str, reset_token: str, frontend_url: Optional[str] = None
) -> bool:
  """비밀번호 재설정 이메일 발송

  Args:
    to_email: 수신자 이메일 주소
    reset_token: 비밀번호 재설정 토큰
    frontend_url: 프론트엔드 URL (비밀번호 재설정 페이지 링크 생성용)

  Returns:
    발송 성공 여부
  """
  try:
    # SMTP 설정이 없으면 로그만 출력 (개발 환경)
    if not settings.SMTP_HOST or not settings.SMTP_USER:
      print('[EMAIL] 비밀번호 재설정 이메일 발송 (개발 모드)')
      print(f'[EMAIL] 수신자: {to_email}')
      print(
        f'[EMAIL] 재설정 링크: {frontend_url or "http://localhost:3000"}/reset-password?token={reset_token}'
      )
      return True

    # 이메일 메시지 생성
    msg = MIMEMultipart('alternative')
    msg['Subject'] = '비밀번호 재설정 요청'
    msg['From'] = settings.SMTP_FROM_EMAIL or settings.SMTP_USER
    msg['To'] = to_email

    # 비밀번호 재설정 링크 생성
    reset_url = f'{frontend_url or settings.FRONTEND_URL or "http://localhost:3000"}/reset-password?token={reset_token}'

    # 텍스트 버전
    text_content = f"""비밀번호 재설정 요청

아래 링크를 클릭하여 비밀번호를 재설정하세요:
{reset_url}

이 링크는 15분간 유효합니다.
만약 비밀번호 재설정을 요청하지 않으셨다면 이 이메일을 무시하세요.
"""

    # HTML 버전
    html_content = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body {{
      font-family: Arial, sans-serif;
      line-height: 1.6;
      color: #333;
    }}
    .container {{
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
    }}
    .button {{
      display: inline-block;
      padding: 12px 24px;
      background-color: #007bff;
      color: #ffffff;
      text-decoration: none;
      border-radius: 4px;
      margin: 20px 0;
    }}
    .footer {{
      margin-top: 30px;
      font-size: 12px;
      color: #666;
    }}
  </style>
</head>
<body>
  <div class="container">
    <h2>비밀번호 재설정 요청</h2>
    <p>아래 버튼을 클릭하여 비밀번호를 재설정하세요:</p>
    <a href="{reset_url}" class="button">비밀번호 재설정</a>
    <p>또는 아래 링크를 복사하여 브라우저에 붙여넣으세요:</p>
    <p><a href="{reset_url}">{reset_url}</a></p>
    <p>이 링크는 15분간 유효합니다.</p>
    <p>만약 비밀번호 재설정을 요청하지 않으셨다면 이 이메일을 무시하세요.</p>
    <div class="footer">
      <p>이 이메일은 자동으로 발송되었습니다.</p>
    </div>
  </div>
</body>
</html>
'''

    # 메시지 본문 추가
    msg.attach(MIMEText(text_content, 'plain', 'utf-8'))
    msg.attach(MIMEText(html_content, 'html', 'utf-8'))

    # SMTP 서버 연결 및 이메일 발송
    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
      if settings.SMTP_USE_TLS:
        server.starttls()
      if settings.SMTP_USER and settings.SMTP_PASSWORD:
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
      server.send_message(msg)

    print(f'[EMAIL] 비밀번호 재설정 이메일 발송 성공: {to_email}')
    return True

  except Exception as e:
    print(f'[EMAIL] 이메일 발송 실패: {to_email}, 오류: {str(e)}')
    return False
