from django import forms


class NameForm(forms.Form):
    # TextInput
    your_name = forms.CharField(label="Your name", max_length=100)

    # Textarea
    # your_name = forms.CharField(label="Your name", max_length=100, widget=forms.Textarea)

    """
    렌더링 결과에는 <form> 태그나 submit 버튼이 없으므로 직접 넣어줘야됨
    <label for="your_name">Your name: </label>
    <input id="your_name" text="text" name="your_name" maxlength="100">
    """


"""
장고의 모든 폼 클래스는 is_valid() 메소드를 가짐.
모든 필드에 대해 유효성 검사 후,
모든 필드가 유효하면
return True, 폼 데이터를 cleaned_data 속성에 넣음.
"""
