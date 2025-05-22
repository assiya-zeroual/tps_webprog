package com.example.businesscard

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Email
import androidx.compose.material.icons.filled.LocationOn
import androidx.compose.material.icons.filled.Phone
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.TileMode
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.tooling.preview.Preview
import com.example.myapplication.R
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.geometry.Offset

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = Color.White
                ) {
                    BusinessCard()
                }
            }
        }
    }
}

@Composable
fun BusinessCard() {
    // Dégradé beige pour le texte
    val beigeGradient = Brush.linearGradient(
        colors = listOf(Color(0xFFF5F5DC), Color(0xFFEEE8AA)),
        start = Offset(0f, 0f),
        end = Offset(100f, 100f),
        tileMode = TileMode.Clamp
    )

    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp)
            .background(Color(0xFF001F3F), shape = RoundedCornerShape(12.dp)) // Bleu marine
            .padding(16.dp)
    ) {
        // Partie gauche : logo, nom, titre
        Column(
            modifier = Modifier
                .weight(1f)
                .padding(end = 16.dp),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Image(
                painter = painterResource(id = R.drawable.ic_launcher_foreground),
                contentDescription = "Logo",
                modifier = Modifier.size(64.dp),
                contentScale = ContentScale.Fit
            )
            Spacer(modifier = Modifier.height(16.dp))
            Text(
                text = "Zeroual Assiya",
                fontSize = 20.sp,
                fontWeight = FontWeight.Bold,
                style = TextStyle(brush = beigeGradient),
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
            Text(
                text = "Software and data Engineer",
                fontSize = 11.sp,
                style = TextStyle(brush = beigeGradient),
                maxLines = 1,
                overflow = TextOverflow.Ellipsis
            )
        }

        // Partie droite : infos contact
        Column(
            modifier = Modifier.weight(1f),
            verticalArrangement = Arrangement.Center
        ) {
            ContactRow(Icons.Default.Phone, "+1 234 567 890", beigeGradient)
            ContactRow(Icons.Default.Email, "Zeroual.Assiya@email.com", beigeGradient)
            ContactRow(Icons.Default.LocationOn, "Morocco", beigeGradient)
        }
    }
}

@Composable
fun ContactRow(icon: ImageVector, contactText: String, textBrush: Brush) {
    Row(
        verticalAlignment = Alignment.CenterVertically,
        modifier = Modifier.padding(vertical = 4.dp)
    ) {
        Icon(
            imageVector = icon,
            contentDescription = null,
            tint = Color(0xFFF5F5DC), // beige clair uniforme pour les icônes
            modifier = Modifier.size(20.dp)
        )
        Spacer(modifier = Modifier.width(8.dp))
        Text(
            text = contactText,
            fontSize = 14.sp,
            style = TextStyle(brush = textBrush)
        )
    }
}

@Preview(showBackground = true)
@Composable
fun BusinessCardPreview() {
    MaterialTheme {
        BusinessCard()
    }
}