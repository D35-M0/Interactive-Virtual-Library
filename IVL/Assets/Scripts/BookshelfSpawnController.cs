using UnityEngine;
using System.Collections;

public class BookshelfSpawnController : MonoBehaviour {

    //public objects
    public GameObject bookshelf, book, //prefab references for bookshelf and book
        spawnCore; //references to a central bookshelf spawn reference and the top left of a bookshelf
    public Transform[] spawnPoints; //array of spawnpoints
    public float shelfY, shelfX, shelfZ; //distance between shelves and distances between books on the same shelf, respectively

    //private objects
    GameObject[] bookshelves; //array of bookshelves
    GameObject[,,] books; //first index is bookshelf, second index is shelf on bookshelf from top, third index is order from left on shelf
    Quaternion bookshelfRotation; //Quaternion to keep the bookshelf rotation consistent
    float bookWidth = 2f; //maximum increase in Z scale to make books appear larger
    int shelfNum = 4, bookNum = 10; //number of shelves on each bookshelf and number of books on each shelf
    Transform bookSpawnPos; //position of the book reference point
    Color[] colors = { Color.red, Color.blue, Color.green, Color.black, Color.cyan, Color.grey };

    void Start()
    {
        bookshelfRotation = spawnCore.transform.rotation;
        bookshelves = new GameObject[spawnPoints.Length];
        books = new GameObject[bookshelves.Length, shelfNum, bookNum];
        Spawn();
    }

    void LateUpdate()
    {
        spawnCore.transform.rotation = bookshelfRotation;
    }

    void Spawn()
    {
        for (int i = 0; i < spawnPoints.Length; i++)
        {
            bookshelves[i] = (GameObject)Instantiate(bookshelf, spawnCore.transform.position, spawnCore.transform.rotation);
            bookshelves[i].transform.parent = spawnCore.transform;

            bookSpawnPos = bookshelves[i].transform.GetChild(0);
            for (int j = 0; j < shelfNum; j++)
            {
                //float offsetY = (shelfY * j) + 1;
                for (int k = 0; k < bookNum; k++)
                {
                    //float offsetX = shelfX * k;
                    //float offsetZ = shelfZ * k;
                    //Vector3 finalPos = new Vector3(offsetX, offsetY, offsetZ);
                    books[i, j, k] = (GameObject)Instantiate(book, bookSpawnPos.position, bookSpawnPos.rotation);
                    books[i, j, k].transform.parent = bookshelves[i].transform;
                    float ypos = books[i, j, k].transform.position.y - (shelfY * (j + 1)) / 4;
                    float xpos = books[i, j, k].transform.position.x + (shelfX * k) / 4;
                    float zpos = books[i, j, k].transform.position.z + (shelfZ * k) / 4;
                    books[i, j, k].transform.position = new Vector3(xpos, ypos, zpos);
                    books[i, j, k].transform.localScale = new Vector3(1f, 1f, Random.Range(1f, 2f));
                    books[i, j, k].transform.GetChild(0).GetComponent<Renderer>().material.color = colors[Random.Range(0,colors.Length)];
                }
            }

            bookshelves[i].transform.position = spawnPoints[i].transform.position;
            bookshelves[i].transform.rotation = spawnPoints[i].transform.rotation;
        }
    }

}