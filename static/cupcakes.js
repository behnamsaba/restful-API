baseUrl = "http://127.0.0.1:5000"

async function getData(){
    const res=await axios.get(baseUrl+"/api/cupcakes")

    for(let x of res.data.cupcakes){
        $(".list").append(`<li data-id=${x.id}>${x.flavor}</li>`);
    }
}


$("form").on("submit",async function (evt){
    evt.preventDefault();
    let flavor=$('input[name="flavor"]').val();
    let size=$('input[name="size"]').val();
    let rating=$("input[name='rating'").val();
    let image=$("input[name='image'").val();
    const postData = await axios.post('http://127.0.0.1:5000/api/cupcakes', {
        flavor,
        rating,
        size,
        image
      });
      $('.list').append(`<li data-id=${postData.data.cupcake.id}>${postData.data.cupcake.flavor}</li>`)
})

getData();