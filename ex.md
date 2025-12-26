UserInfo = 테이블 => {
  id: number;
  name: string;
}

UserVo = 밸류 오브젝트 => {
  id: number;
  name: string;
  idList: number[];
}

// 스프링부트로 치면 컨트롤러. 현재 프로젝트 구조에서는 라우터에 해당함.
getUserList(userVo: UserVo) => {
  service.getUserList(userVo); // 이렇게만 전달을 해도 되게끔.
}

// 여러개의 필드를 전달하는 게 아닌 하나만 전달할 때에는 그냥 이렇게 하나만 전달해도 됨.
getUserByNo(userId: number) => {
  service.getUserByNo(userId); // 이렇게만 전달을 해도 되게끔.
}

createUser(userVo: UserVo) => {
  service.createUser(userVo);
}

즉, 겟이든 포스트든 뭐든 vo 만 넘기면 알아서 그 vo에서 뭘 꺼내든 뭘 하든 해서 데이터를 처리하는 것.

밸류 오브젝트는 검색할 때에도 사용하고 데이터를 body 에 실어서 보낼 때에도 사용함.
스프링 부트에는 프론트에서 객체를 전달하면 자동으로 vo에 할당해주는 기능이 있었는데 파이썬에도 그 기능이 있는지는 모르겠으나, 아무튼 이런 느낌을 원하는 것.