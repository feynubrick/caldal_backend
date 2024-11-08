Feature: 스케쥴 그룹 생성 테스트
  Background:
    Given 이메일이 "a@gmail.com"인 사용자가 "google" 로그인으로 회원가입했습니다.

  Scenario: 사용자는 스케쥴 그룹을 만들 수 있다.
    When 이메일이 "a@gmail.com"인 사용자가 스케쥴 그룹 생성을 요청합니다.
      """
      {
        "name": "업무",
        "color": "#D3BFD9"
      }
      """
    Then 서버의 응답 상태코드는 201입니다.
    And 응답 내용은 다음과 같습니다.
      """
      {
        "name": "업무",
        "color": "#D3BFD9",
        "is_default": false,
        "order_index": 1
      }
      """

  Scenario: 스케쥴 그룹이 생성될 때 order_index는 1씩 증가한다.
    Given 이메일이 "a@gmail.com"인 사용자가 10번 스케쥴 그룹 생성을 요청합니다.
    Then 이메일이 "a@gmail.com"인 사용자가 마지막으로 만든 스케쥴 그룹의 order_index는 10이고, 만들어진 순서대로 1씩 차이가 납니다.

  Scenario Outline: 잘못된 컬러코드를 보낼 수 없다.
    When 이메일이 "a@gmail.com"인 사용자가 스케쥴 그룹 생성을 요청합니다.
      """
      {
        "name": "업무",
        "color": "<color>"
      }
      """
    Then 서버의 응답 상태코드는 422입니다.
    Examples:
    | color    |
    | D3BFD9   |
    | #D3BFD   |
    | #D3BFD99 |
