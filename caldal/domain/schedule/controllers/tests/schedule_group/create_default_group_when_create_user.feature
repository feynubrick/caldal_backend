Feature: 사용자 생성시 기본 스케쥴 그룹 만들기
  Background:
    Given 이메일이 "a@gmail.com"인 사용자가 "google" 로그인으로 회원가입했습니다.

  Scenario: 사용자가 회원 가입할 때 기본 스케쥴 그룹이 생성된다.
    When 이메일이 "a@gmail.com"인 사용자가 스케쥴 그룹 목록을 요청합니다.
    Then 서버의 응답 상태코드는 200입니다.
    And 응답으로 돌아온 스케쥴 그룹 목록은 다음과 같습니다.
      """
      [
        {
          "name": "기본",
          "color": "#D3BFD9",
          "order_index": 0,
          "is_default": true
        }
      ]
      """
