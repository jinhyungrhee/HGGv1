import string
from django.core.exceptions import ValidationError

def contains_special_character(value):
    for char in value:
        if char in string.punctuation: # string.punctuation : 특수문자를 모아놓은 문자열
            return True
    return False

def validate_no_special_characters(value):
    if contains_special_character(value): # 특수문자 있는지 체크
        raise ValidationError("특수문자를 포함할 수 없습니다.") # 있으면 validation error 발생시킴

# 학교 계정 여부 확인
def validate_hufs_email(email):
    if not email.endswith('hufs.ac.kr'):
        raise ValidationError("학교 계정으로만 가입이 가능합니다")


# Custom Password Validator
def contains_uppercase_letter(value):
    return True

def contains_lowercase_letter(value):
	return True

def contains_number(value):
    return True

class CustomPasswordValidator: # 비밀번호에 대한 validator(클래스 형태) - 이외의 대부분은 함수형 validator 사용
    def validate(self, password, user=None):
        if (
                len(password) < 8 or
                not contains_uppercase_letter(password) or
                not contains_lowercase_letter(password) or
                not contains_number(password) or
                not contains_special_character(password)
        ):
            raise ValidationError("8자 이상의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다.")

    def get_help_text(self): # admin에서 비밀번호를 바꿀 때 필요한 내용
        return "8자 이상의 영문 대/소문자, 숫자, 특수문자 조합을 입력해 주세요."