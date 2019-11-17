const uploadAudio = document.getElementById('recorder');
const [spinner] = document.querySelectorAll('.spinner');

const transcribeUrl = '/transcribe';

uploadAudio.addEventListener('change', async (event) => {
    let response
    try {
        const [audioFile] = event.target.files;
        const formData = new FormData();
        formData.append('file', audioFile);

        uploadAudio.disabled = true;
        spinner.style.display = 'block';

        const options = {
            method: 'POST',
            mode: 'same-origin',
            cache: 'no-cache',
            body: formData
        }

        const _response = await fetch(transcribeUrl, options);
        response = await _response.json()
    } catch (error) {
        console.error(error);
    } finally {
        uploadAudio.disabled = false;
        spinner.insertAdjacentHTML('afterend', response.template);
        spinner.style.display = 'none';
    }
})
