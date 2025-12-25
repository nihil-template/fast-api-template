from enum import Enum
from typing import Optional

from sqlalchemy import Column, Integer, String, text
from sqlalchemy import Enum as SQLEnum
from sqlmodel import Field, SQLModel

# UTC 타임스탬프 포맷팅 SQL 함수
UTC_TIMESTAMP_FORMAT = (
  'to_char(current_timestamp AT TIME ZONE \'UTC\', \'YYYY-MM-DD"T"HH24:MI:SS"Z"\')'
)


class UserRole(str, Enum):
  USER = 'USER'


class YnStatus(str, Enum):
  Y = 'Y'
  N = 'N'


class UserInfo(SQLModel, table=True):
  __tablename__ = 'user_info'

  userNo: Optional[int] = Field(
    default=None, sa_column=Column('user_no', Integer, primary_key=True)
  )

  emlAddr: str = Field(sa_column=Column('eml_addr', String, unique=True))

  userNm: str = Field(sa_column=Column('user_nm', String, unique=True))

  userRole: UserRole = Field(
    default=UserRole.USER,
    sa_column=Column('user_role', SQLEnum(UserRole), default=UserRole.USER),
  )

  proflImg: Optional[str] = Field(
    default=None, sa_column=Column('profl_img', String, nullable=True)
  )

  userBiogp: Optional[str] = Field(
    default=None, sa_column=Column('user_biogp', String, nullable=True)
  )

  encptPswd: str = Field(sa_column=Column('encpt_pswd', String))

  reshToken: Optional[str] = Field(
    default=None, sa_column=Column('resh_token', String, nullable=True)
  )

  useYn: YnStatus = Field(
    default=YnStatus.Y,
    sa_column=Column('use_yn', SQLEnum(YnStatus), default=YnStatus.Y),
  )

  delYn: YnStatus = Field(
    default=YnStatus.N,
    sa_column=Column('del_yn', SQLEnum(YnStatus), default=YnStatus.N),
  )

  lastLgnDt: Optional[str] = Field(
    default=None,
    sa_column=Column(
      'last_lgn_dt',
      String,
      nullable=True,
      server_default=text(UTC_TIMESTAMP_FORMAT),
    ),
  )

  lastPswdChgDt: Optional[str] = Field(
    default=None,
    sa_column=Column(
      'last_pswd_chg_dt',
      String,
      nullable=True,
      server_default=text(UTC_TIMESTAMP_FORMAT),
    ),
  )

  crtNo: Optional[int] = Field(
    default=None, sa_column=Column('crt_no', Integer, nullable=True)
  )

  crtDt: str = Field(
    sa_column=Column(
      'crt_dt',
      String,
      server_default=text(UTC_TIMESTAMP_FORMAT),
    )
  )

  updtNo: Optional[int] = Field(
    default=None, sa_column=Column('updt_no', Integer, nullable=True)
  )

  updtDt: str = Field(
    sa_column=Column(
      'updt_dt',
      String,
      server_default=text(UTC_TIMESTAMP_FORMAT),
    )
  )

  delNo: Optional[int] = Field(
    default=None, sa_column=Column('del_no', Integer, nullable=True)
  )

  delDt: Optional[str] = Field(
    default=None, sa_column=Column('del_dt', String, nullable=True)
  )
