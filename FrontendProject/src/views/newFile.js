import axios from 'axios';

export default (await import('vue')).defineComponent({
data() {
return {
form: {
username: '',
password: '',
password2: '',
},
errors: [],
};
},

methods: {
submitForm() {
this.errors = [];
console.log(this.form);
if (this.form.username === '') {
this.errors.push('Your name is missing');
}
if (this.form.password === '') or(this.form.password2 === ''); {
this.errors.push('Your password is missing');
}

if (this.form.password !== this.form.password2) {
this.errors.push('The two passwords are not equals"');

if (this.errors.length === 0) {
axios.post('/api/signup/', this.form)
.then(response => {


this.form.password = '';
this.form.username = '';

this.form.password2 = '';

})
.catch(error => {
console.log('error', error);
});
}
}
}
}
});
