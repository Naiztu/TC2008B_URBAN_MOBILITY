using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class UrbanMobility : MonoBehaviour
{
    public GameObject Carro;
    public GameObject AltCarro;

    public GameObject[] selectorArr;
    public GameObject selector;
    public TextMeshProUGUI agentText;

    public float timeToUpdate = 5.0f;
    private float timer;
    float dt;

    IEnumerator GetData()
    {
        Agent a = APIHelper.GetNewAgent();

        for (int i = 0; i < a.positions.Count; i++)
        {
            Debug.Log("Llego al loop");
            if (i != a.positions[i].unique_id)
            {
                continue;
            }
            Debug.Log("Paso al loop if");
            GameObject car = Instantiate(Carro, new Vector3(a.positions[i].pos.x, 0, a.positions[i].pos.y), Quaternion.identity);
            car.GetComponent<Movement>().ID = a.positions[i].unique_id; // Corregir posiciones de "i" a pasar.
            car.GetComponent<Movement>().previousPosy = a.positions[i].pos.y - 3;
            car.GetComponent<Movement>().posy = a.positions[i].pos.y;

        }

        yield return null;

    }

    /*public void NewAgent()
    {
        Agent a = APIHelper.GetNewAgent();
        agentText.text = a.step_count.ToString();

        for (int i = 0; i < a.positions.Count; i++)
        {
            Debug.Log("IDS: " + a.positions[i].unique_id);

            // Debug.Log("X: " + a.positions[i].pos.x);
            // Debug.Log("Y: " + a.positions[i].pos.y);

        }

        Debug.Log("NUM CARROS = " + a.state_num_cars);

    }*/


    void Start()
    {
#if UNITY_EDITOR
        StartCoroutine(GetData());
        timer = timeToUpdate;
#endif

    }

    void Update()
    {

        timer -= Time.deltaTime;
        dt = 1.0f - (timer / timeToUpdate);

        if (timer < 0)
        {

#if UNITY_EDITOR
            timer = timeToUpdate; // reset the timer
            /*Vector3 fakePos = new Vector3(3.44f, 0, -15.707f);
            string json = EditorJsonUtility.ToJson(fakePos);*/
            StartCoroutine(GetData());
#endif
        }

    }

}