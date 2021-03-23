1. noUiSlider: https://refreshless.com/nouislider/behaviour-option/
2. noUiSlider and input section: https://stackoverflow.com/questions/33366971/replace-hidden-field-value-with-value-of-nouislider-value-to-pass-to-form-php
3. noUiSlider slider "snap: true," for nolinear case
4. scroll css and js example: https://stackoverflow.com/questions/55399726/how-to-create-a-button-to-go-back-to-the-top-of-the-page
5. materialize for textarea with outline somehow not work well
6. For textarea upload, request.form.get('name')
7. everytime need to refresh the webpage to take effect
8. html name can be the same, but ID should be different in case of a JS <script> with getID.
9. For upoading files, need to add: enctype = "multipart/form-data"
10. For convert byte to string: file.read().decode("utf-8") 
11. For upoading files, Use request.files['name'].filename == '' to check whether it is uploaded
12. Submit with a progress bar: add onclick="$('#progressBar_g').show();" in submit button; add style="display:none;" in progress bar.
13. After modifying config.py file, should restart flask
14. Remove app.db and migrations/ before falsk db init
15. Transfer from HTML to python flask:
```python
  @web.route('/sth_<string:blog_name>')
  def sth(blog_name):
```
be are do not use:
```python
sth/<string:blog_name>
```
otherwise the style do not work.

16. Use another URL in form submit:
```html
<input type="submit" value="Go Elsewhere" formaction="/elsewhere">
```
