import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import globalComponents from './components/common/global-components'
import PrimeVue from 'primevue/config'
import Carousel from 'primevue/carousel'

const app = createApp(App)


globalComponents.forEach(component => {
    app.component(component.name, component)
})
app.use(router)
app.use(PrimeVue)
app.component('Carousel', Carousel)

app.mount('#app')
