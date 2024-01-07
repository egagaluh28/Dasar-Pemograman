const password = document.getElementById('password')
const username = document.getElementById('username')

document.getElementById('form').addEventListener('submit' , (event) => {
    event.preventDefault()
    valid=true
    
    // add your checks here :

    const password_value = password.value 
    const username_value = username.value 

    if (username_value.length < 5 || password_value.length < 12){
        alert('the form has not been submitted : \n - A field is not valid')
        valid = false
    }

    if (valid) 
        alert('the form has been complited. \n we will proceed with the sending')
    
})