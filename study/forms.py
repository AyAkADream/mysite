from django import forms

class study_PostForm(forms.Form):
    #title = forms.CharField(max_length=30, label='タイトル')
    #content = forms.CharField(label='内容' , widget=forms.Textarea())

    title = forms.CharField(max_length=200, label='タイトル', required=False)
    author = forms.CharField(label='著者と所属のリスト', widget=forms.Textarea(),required=False)
    content = forms.CharField(label='どんなもの？' , widget=forms.Textarea(), required=False)
    url1_title = forms.CharField(max_length=100, label='URL1のタイトル', required=False)
    url1 = forms.CharField(max_length=100, label='URL1', required=False)
    url2_title = forms.CharField(max_length=100, label='URL2のタイトル', required=False)
    url2 = forms.CharField(max_length=100, label='URL2', required=False)
    url3_title = forms.CharField(max_length=100, label='URL3のタイトル', required=False)
    url3 = forms.CharField(max_length=100, label='URL3', required=False)
    url4_title = forms.CharField(max_length=100, label='URL4のタイトル', required=False)
    url4 = forms.CharField(max_length=100, label='URL4', required=False)
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
    comparison = forms.CharField(label='先行研究と比べてどこがすごい？' , widget=forms.Textarea(), required=False)
    key = forms.CharField(label='技術や手法のキモはどこ？' , widget=forms.Textarea(), required=False)
    experiment = forms.CharField(label='どうやって有効だと検証した？' , widget=forms.Textarea(), required=False)
    discussion = forms.CharField(label='議論はある？' , widget=forms.Textarea(), required=False)
    next_paper = forms.CharField(label='次に読むべき論文は？' , widget=forms.Textarea(), required=False)
    thoughts = forms.CharField(label='この論文について、どう思う？' , widget=forms.Textarea(), required=False)
    memo = forms.CharField(label='その他・メモ' , widget=forms.Textarea(), required=False)
    