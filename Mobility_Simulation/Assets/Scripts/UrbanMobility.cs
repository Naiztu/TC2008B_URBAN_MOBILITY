using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class UrbanMobility : MonoBehaviour
{
    public TextMeshProUGUI agentText;
    public void NewAgent(){
        Agent a = APIHelper.GetNewAgent();
        agentText.text = a.step_count.ToString();

        Debug.Log("Height = " + a.height + "\nMax_Carros = " + a.max_num_cars + "\nTiempo = " + a.time);

    }

}