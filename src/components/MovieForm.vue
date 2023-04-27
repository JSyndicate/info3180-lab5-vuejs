<template>
    <form id="MovieForm" @submit.prevent="saveMovie">
        <div class = "form-group mb-3">.
            <label for="title" class="form-label">Movie Title</label>
            <input type="text" name="title" class="form-control"/>
            <label for="title" class="form-label">Description</label>
            <input type="text" name="description" class="form-control"/>
            <label for="impage-poster">Poster</label>
            <input type="file" class="form-control-file" id="image-poster"/>
            <button type="submit">Upload</button>
        </div>
    </form>
</template>

<script setup>

    import { ref, onMounted } from "vue";
    
    onMounted(() => {
        getCsrfToken();
    });

    let csrf_token = ref("");
      
        function getCsrfToken(){
                
            fetch('/ap1/v1/csrf-token')
                .then((response) => response.json())
                .then((data) => {
                    console.log(data);
                    csrf_token.value = data.csrf_token;
                })
        }


      function saveMovie(){

        let MovieForm = document.getElementById('MovieForm');
        let form_data = new FormData(MovieForm);
        

        fetch("/api/v1/movies",{
            method:'POST',
            body: form_data,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                flash('Successful')
                console.log(data)
            })
            .catch(function (error) {
                console.log(error);
            });
      }

</script>