# Jinja

---

## What is Jinja?

---

### Jinja is

- **Fast expressive and extensible templating language.**
- **Able to write code similar to Python in the DOM (Document Object Model).**
- **Used in Flask, Django, Ansible, and SaltStack.**
- **The template is passed data to render within the final document.**

---

## What are Jinja templating tags and scripts?

---

- **Jinja tags allows developers to be confident while working with backend data, using tags that are similar to HTML.**

```html
<link
  rel="stylesheet" type="text/css"
  href="{{ url_for('static', path='/todo/css/base.css' )}}"
>
</link>
```

- **Now image we have list of `todos` that we retrieved from the database. We can pass the entire list of `todos` into the front-end and loop through each todo with this simple `for loop` on the template.**

```python
# in backend
context: {
    "todos": todo_list
}
# this will be passed to the front-end
```

```html
<!-- in front-end -->
{% for todo in todos %}
  <li>Do something with todo</li>
{% endfor %}
```

- **We can also use Jinja templating language with `if else` statements. One thing that may stand out is the double brackets with `todos|length`.**

```html
{% if todos %}
    Display: {{ todos|length }} Todos
{% else %}
    You don't have any todos
{% endif %}
```
