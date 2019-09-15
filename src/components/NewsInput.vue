<template>
    <div id="newsInput">
        <v-container fluid class="newsInput-container">
            <v-layout column align-center>
            <v-flex xs4 justify-center>
                <h2 text class="newInput-title pink--text text--lighten-3"> Let us find out Who is lying </h2>
            </v-flex>
            <v-flex xs3>
                <form class="newsInput-form">
                    <v-text-field
                    v-model="name"
                    :error-messages="nameErrors"
                    :counter="10"
                    label="Name"
                    required
                    @input="$v.name.$touch()"
                    @blur="$v.name.$touch()"
                    color="#26C6DA"
                    ></v-text-field>
                    <v-text-field
                    v-model="email"
                    :error-messages="emailErrors"
                    label="E-mail"
                    required
                    @input="$v.email.$touch()"
                    @blur="$v.email.$touch()"
                    color="#26C6DA"
                    ></v-text-field>
                    <v-text-field
                    v-model="newsTitle"
                    :error-messages="newsTitleErrors"
                    label="News Title"
                    required
                    @input="$v.newsTitle.$touch()"
                    @blur="$v.newsTitle.$touch()"
                    color="#26C6DA"
                    ></v-text-field>
                    <v-text-field
                    v-model="newsSource"
                    :error-messages="newsSourceErrors"
                    label="News Original Source"
                    required
                    @input="$v.newsSource.$touch()"
                    @blur="$v.newsSource.$touch()"
                    color="#26C6DA"
                    ></v-text-field>
                    <v-textarea
                    counter
                    v-model="newsContent"
                    :error-messages="newsContentErrors"
                    required
                    label="News Content"
                    :rules="rules"
                    :value="value"
                    color="#26C6DA"
                    no-resize
                    ></v-textarea>
                </form>
            </v-flex>
            <v-flex xs4>
                <button class="newsInput-go newsInput-clear" @click="clear">Clear</button>
                <router-link to="/ShowResult"><button class="newsInput-go">Go!</button></router-link>
            </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, maxLength, email } from 'vuelidate/lib/validators'

export default {
mixins: [validationMixin],

validations: {
    name: { required, maxLength: maxLength(10) },
    email: { required, email },
    newsTitle: { required },
    newsSource: { required },
    newsContent: { required }
},

data: () => ({
    name: '',
    email: '',
    newsTitle: '',
    newsSource: '',
    newsContent: 'Hello! Type in the news content you want to check.',
}),

computed: {
    nameErrors () {
        const errors = []
        if (!this.$v.name.$dirty) return errors
        !this.$v.name.maxLength && errors.push('Name must be at most 10 characters long')
        !this.$v.name.required && errors.push('Name is required.')
        return errors
    },
    emailErrors () {
        const errors = []
        if (!this.$v.email.$dirty) return errors
        !this.$v.email.email && errors.push('Must be valid e-mail')
        !this.$v.email.required && errors.push('E-mail is required')
        return errors
    },
    newsTitleErrors () {
        const errors = []
        if (!this.$v.newsTitle.$dirty) return errors
        !this.$v.newsTitle.required && errors.push('News Title is required')
        return errors
    },
    newsSourceErrors () {
        const errors = []
        if (!this.$v.newsSource.$dirty) return errors
        !this.$v.newsSource.required && errors.push('News Original Source is required')
        return errors
    },
    newsContentErrors () {
        const errors = []
        if (!this.$v.newsContent.$dirty) return errors
        !this.$v.newsContent.required && errors.push('News Content is required')
        return errors
    }

},

methods: {
    submit () {
    this.$v.$touch()
    },
    clear () {
        this.$v.$reset()
        this.name = ''
        this.email = ''
        this.newsTitle = ''
        this.newsSource = ''
        this.newsContent = 'Hello! Type in the news content you want to check.'
    },
},
}
</script>

<style>
#newsInput {
    font-family: 'Geo', sans-serif;
    height: 92vh;
    background: white;
}
.newsInput-container {
    height: 90vh;
    padding: 35px 0;
    background: white;
}
.newInput-title {
    font-size: 30px;
}
.newsInput-form {
    margin: 30px 0;
    padding: 30px;
    border-radius: 20px;
    border: #C0CA33 solid 1px;
    width: 40vw;
    background: white;
    color: #26C6DA;
}
.newsInput-textarea {
    color: white;
}
.newsInput-go {
    font-size: 18px;
    border-radius: 50px;
    border: solid #F48FB1 1px;
    padding: 5px 40px;
    margin: 2.5vh 20px;
    outline: none;
    box-shadow: 3px 3px 6px rgb(123, 123, 123);
    background:  white;
    color: #F48FB1;
    transition: 0.8s;
}
.newsInput-go:hover{
    border-radius: 50px;
    border: solid #F48FB1 1px;
    padding: 5px 40px;
    margin: 2.5vh 20px;
    outline: none;
    box-shadow: 0 1px 5px rgb(123, 123, 123);
    background:  #F48FB1;
    color: white;
    transition: 0.8s;
}
.newsInput-clear {
    border: solid #26C6DA 1px;
    color: #26C6DA;
}
.newsInput-clear:hover {
    border: solid #26C6DA 1px;
    background:  #26C6DA;
}
.newsInput-footer {
    height: 10vh;
}
</style>