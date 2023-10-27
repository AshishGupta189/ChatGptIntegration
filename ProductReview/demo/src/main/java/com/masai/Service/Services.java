package com.masai.Service;

import java.util.List;

import com.masai.DTO.ProductDTO;
import com.masai.DTO.ReviewDTO;
import com.masai.Entity.Product;
import com.masai.Entity.Review;
import com.masai.Exception.ProductException;
import com.masai.Exception.ReviewException;

public interface Services {
	
	public String addProduct(ProductDTO product);
	public List<Product> getAllProduct() throws ProductException;
	public Product getProductById(Integer id)throws ProductException;
	public String updateProduct(Integer id,ProductDTO product)throws ProductException;
	public String deleteProduct(Integer id)throws ProductException;
	public String createReview(Integer pId,ReviewDTO review)throws ProductException,ReviewException;
	public String deleteReview(Integer pId,Integer rId)throws ProductException,ReviewException;
	public List<Review> getReviewforProduct(Integer pid) throws ProductException,ReviewException;

}
