package com.masai.Repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.masai.Entity.Review;

@Repository
public interface ReviewDao extends JpaRepository<Review, Integer>{

}
