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

    /*IEnumerator GetData()
    {
        Agent a = APIHelper.GetNewAgent();

        int ids = 0;

        for (int i = 0; i < a.positions.Count; i++){
            if (i = a[i].positions.unique_id){
                ids += 1;
            }
        }

        for (int j = 0; j < ids; j++){
           Instantiate(selector, new Vector3(a.positions[i].pos.x, 0, a.positions[i].pos.y), Quaternion.identity) as GameObject;
           // Otorgarle a cada objeto el unique_id
        }

    }*/

    public void NewAgent()
    {
        Agent a = APIHelper.GetNewAgent();
        agentText.text = a.step_count.ToString();

        for (int i = 0; i < a.positions.Count; i++)
        {
            Debug.Log("IDS: " + a.positions[i].unique_id);

            // Debug.Log("X: " + a.positions[i].pos.x);
            // Debug.Log("Y: " + a.positions[i].pos.y);

        }

        Debug.Log("NUM CARROS= " + a.state_num_cars);

    }


    void Start()
    {

    }

    void Update()
    {

    }

}