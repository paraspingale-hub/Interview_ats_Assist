package com.paraspingale.portfolio;

import java.util.Map;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:5173")
public class ProfileController {
  @GetMapping("/profile")
  public Map<String, String> profile() {
    return Map.of("name", "Paras Rahul Pingale", "location", "Pune, Maharashtra, India");
  }
}
