using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class UrbanMobility : MonoBehaviour
{
    public float timeToUpdate = 5.0f;
    private float timer;
    float dt;

    public GameObject Carro;
    public GameObject AltCarro;

    int numCar;

    // IEnumerator - yield return
    IEnumerator SendData()
    {
        WWWForm form = new WWWForm();
        form.AddField("bundle", "the data");
        string url = "http://127.0.0.1:5000/step";
        using (UnityWebRequest www = UnityWebRequest.Get(url))
        {
            www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
            www.SetRequestHeader("Content-Type", "application/json");

            yield return www.SendWebRequest();          // Talk to Python
            if (www.isNetworkError || www.isHttpError)
            {
                Debug.Log("Hola");
                Debug.Log(www.error);
            }
            else
            {
                Agent a = JsonUtility.FromJson<Agent>(www.downloadHandler.text);
                Debug.Log(a.step_count);

                for (int i = 0; i < a.positions.Count; i++)
                {
                    //Debug.Log("Llego al loop " + i);

                    numCar = GameObject.FindGameObjectsWithTag("Player").Length;

                    if (numCar != a.state_num_cars)
                    {

                        GameObject car = Instantiate(Carro, new Vector3(a.positions[i].pos.x, 0, a.positions[i].pos.y), Quaternion.identity);
                        car.GetComponent<Movement>().ID = a.positions[i].unique_id; // Corregir posiciones de "i" a pasar.
                        car.GetComponent<Movement>().previousY = a.positions[i].pos.y - 3;
                        car.GetComponent<Movement>().posY = a.positions[i].pos.y;

                    }
                    /*Debug.Log("Paso al loop if");
                    GameObject car = Instantiate(Carro, new Vector3(a.positions[i].pos.x, 0, a.positions[i].pos.y), Quaternion.identity);
                    car.GetComponent<Movement>().ID = a.positions[i].unique_id; // Corregir posiciones de "i" a pasar.
                    car.GetComponent<Movement>().previousY = a.positions[i].pos.y - 3;
                    car.GetComponent<Movement>().posY = a.positions[i].pos.y;*/
                }
            }
        }

    }

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        timer -= Time.deltaTime;
        dt = 1.0f - (timer / timeToUpdate);

        if (timer < 0)
        {
#if UNITY_EDITOR
            timer = timeToUpdate; // reset the timer
            StartCoroutine(SendData());
#endif
        }
    }
}