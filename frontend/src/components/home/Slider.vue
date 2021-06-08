<template>
  <!-- Slider Area -->
  <div class="slider-container col-lg-9">
    <div class="content">
      <img v-for="img in slider_images" :key="img.id" 
      :src="'http://127.0.0.1:8000' + img.image" alt="Slider">
    </div>
  </div>
  <!--/ End Slider Area -->
</template>
<script>
import { sendRequest } from '@/views/functions'

export default {
  name: 'slider',
  data () {
    return {
      slider_images: ""
    }
  },
  mounted () {
    this.fetchSliderImages()
  },
  methods: {
    async fetchSliderImages () {
      let req = await sendRequest('server/slider_images/')
      this.slider_images = req.data
    }
  }
}
</script>
<style>
img, div {
  margin: 0;
  padding: 0;
}
.slider-container {
  overflow-x: hidden;
  overflow-y: hidden;
  max-height: 564px; 
}
.slider-container img{
  display: block;
}

.content {
  display: flex;
  margin: 0;
  width: 100%;
  animation: slide 10s ease-in-out infinite;
}

@keyframes slide{
  10%{
    transform: translateX(0);
  }
  15%, 30%{
    transform: translateX(-100%);
  } 
  35%, 50%{
    transform: translateX(-200%);
  }
  55%, 70%{
    transform: translateX(-300%);
  }
  75%, 90%{
    transform: translateX(0);
  }
}
@media (max-width: 990px) {
  .slider-container {
    max-height: 80vh;
    margin: 20px 0;
  }
}
</style>