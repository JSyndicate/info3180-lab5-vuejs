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

      function saveMovie(){

        fetch("/api/v1/movies",{
            method:'POST'
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