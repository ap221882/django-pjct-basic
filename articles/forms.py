from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data =  self.cleaned_data  #It is a dictionary
    #     print("cleaned_data",cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "nepal":
    #         raise forms.ValidationError('This title is taken')
    #     print("title",title)
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print("all data", cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "nepal":
            self.add_error('title','This title is taken!!!!!')  #Field error
            # raise forms.ValidationError('This title is taken') #Non-field error
        if "office" in content:
            raise forms.ValidationError('Office cant be in content')
        return cleaned_data