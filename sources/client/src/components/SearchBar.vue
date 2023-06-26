<!-- SearchBar.vue -->
<template>
    <div class="input-group input-group-lg">
      <input type="text" class="form-control" placeholder="search station">
      <button class="btn btn-outline-secondary" type="button" @click="$emit('search')">search</button>
    </div>
  </template>