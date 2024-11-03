Feature: OAuth 처리
  OAuth 처리하는 API에 대한 테스트

  Scenario Outline: 사용자는 소셜 로그인으로 회원가입할 수 있다.
    Given 이메일이 "a@gmail.com"인 사용자는 존재하지 않습니다.
    When 이메일이 "a@gmail.com"인 사용자가 "<provider>" 로그인으로 회원가입을 요청합니다.
    Then 서버의 응답 상태코드는 201입니다.
    And 다음 정보로 사용자를 한명 찾을 수 있습니다.
      """
      {
        "email": "a@gmail.com",
        "provider": "<provider>"
      }
      """

    Examples:
      | provider |
      | GOOGLE   |

  Scenario Outline: 회원가입한 사용자는 소셜 로그인으로 로그인할 수 있다.
    Given 이메일이 "a@gmail.com"인 사용자가 "<provider>" 로그인으로 회원가입했습니다.
    When 이메일이 "a@gmail.com"인 사용자가 "<provider>" 로그인으로 로그인을 요청합니다.
    Then 서버의 응답 상태코드는 200입니다.
    And 다음 정보로 사용자를 한명 찾을 수 있습니다.
      """
      {
        "email": "a@gmail.com",
        "provider": "<provider>"
      }
      """

    Examples:
      | provider |
      | GOOGLE   |
