using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class UrbanMobility : MonoBehaviour
{
    public TextMeshProUGUI agentText;

    //public int arr = {1, 2, 3, 6};
    public void NewAgent(){
        Agent a = APIHelper.GetNewAgent();
        agentText.text = a.step_count.ToString();

        for(int i = 0; i < a.positions.Count; i++)
        {
            Debug.Log("X: " + a.positions[i].position.x);
           
        }

        Debug.Log("Height = " + a.height + "\nMax_Carros = " + a.max_num_cars + "\nTiempo = " + a.time);

    }

}